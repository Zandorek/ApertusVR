from string import Template
import argparse
import os
from distutils.dir_util import copy_tree

uncapitalize = lambda s: s[:1].lower() + s[1:] if s else ''

class ApePackageManager:
    variable = "blah"

    def __init__(self):
        self.templatesPath = './templates/'

    def createPluginTemplate(self, args):
        pluginName = uncapitalize(args.name)
        pluginPath = '../../plugins/' + pluginName + '/'
        pluginClassName = 'Ape' + pluginName.capitalize() + 'Plugin'

        # create plugin folder
        if not os.path.exists(pluginPath):
            os.makedirs(pluginPath)

        # open plugin header template file
        pluginHeaderFileName = pluginClassName + '.h'
        pluginHeaderFilePath = pluginPath + pluginHeaderFileName
        with open(self.templatesPath + 'plugin_h.template', 'r') as pluginHeaderTemplateFile:
            data = pluginHeaderTemplateFile.read()

            # replace variables in header template
            s = Template(data)
            res = s.substitute(pluginClassName=pluginClassName)
            # print(res)

            # write plugin header file
            with open(pluginHeaderFilePath, "w") as pluginHeaderFile:
                pluginHeaderFile.write(res)

        # open plugin cpp template file
        pluginCppFileName = pluginClassName + '.cpp'
        pluginCppFilePath = pluginPath + pluginCppFileName
        with open(self.templatesPath + 'plugin_cpp.template', 'r') as pluginCppTemplateFile:
            data = pluginCppTemplateFile.read()

            # replace variables in cpp template
            s = Template(data)
            res = s.substitute(pluginClassName=pluginClassName)
            # print(res)

            # write plugin cpp file
            with open(pluginCppFilePath, "w") as pluginCppFile:
                pluginCppFile.write(res)

        # open plugin cmake template file
        pluginCmakeFilePath = pluginPath + 'CMakeLists.txt'
        with open(self.templatesPath + 'plugin_cmake.template', 'r') as pluginCmakeTemplateFile:
            data = pluginCmakeTemplateFile.read()

            # replace variables in cmake template
            s = Template(data)
            res = s.substitute(pluginClassName=pluginClassName, pluginHeaderFileName=pluginHeaderFileName, pluginCppFileName=pluginCppFileName)
            # print(res)

            # write plugin cmake file
            with open(pluginCmakeFilePath, "w") as pluginCmakeFile:
                pluginCmakeFile.write(res)

        print(pluginClassName + ' has been created.')

    def createSampleTemplate(self, args):
        sampleName = uncapitalize(args.name)
        samplePath = '../../samples/' + sampleName + '/'
        configPath = samplePath + 'configs/'
        sampleClassName = 'Ape' + sampleName.capitalize()

        # create sample folder
        if not os.path.exists(samplePath):
            os.makedirs(samplePath)

        # open sample cpp template file
        sampleCppFileName = sampleClassName + '.cpp'
        sampleCppFilePath = samplePath + sampleCppFileName
        with open(self.templatesPath + 'sample_cpp.template', 'r') as sampleCppTemplateFile:
            data = sampleCppTemplateFile.read()

            # replace variables in sample cpp template
            s = Template(data)
            res = s.substitute(sampleName=sampleName)

            # write sample cpp file
            with open(sampleCppFilePath, "w") as sampleCppFile:
                sampleCppFile.write(res)

        copy_tree(self.templatesPath + 'configs/', samplePath + 'configs/')

        # open plugin cmake template file
        with open(self.templatesPath + 'configs/default/CMakeLists.txt', 'r') as sampleDefaultConfigCmakeTemplateFile:
            data = sampleDefaultConfigCmakeTemplateFile.read()

            # replace variables in cmake template
            s = Template(data)
            res = s.substitute(sampleName=sampleName)

            # write plugin cmake file
            with open(configPath + 'default/' + 'CMakeLists.txt', "w") as sampleDefaultConfigCmakeFile:
                sampleDefaultConfigCmakeFile.write(res)


apm = ApePackageManager()

parser = argparse.ArgumentParser(description='Optional app description')
subparsers = parser.add_subparsers(help='sub-command help')

# create the parser for 'status' command
parser_status = subparsers.add_parser('status', help='a help')
parser_status.add_argument('bar', type=int, help='bar help')


# create the parser for 'create' command
parser_create = subparsers.add_parser('create', help='b help')
parser_create_subparsers = parser_create.add_subparsers(help='sub-command help')

# parse plugin arguments
parser_create_plugin = parser_create_subparsers.add_parser('plugin', help='sub-command help')
parser_create_plugin.add_argument('-n', '--name', type=str, help='An optional string argument')
parser_create_plugin.set_defaults(func=apm.createPluginTemplate)

# parse plugin arguments
parser_create_sample = parser_create_subparsers.add_parser('sample', help='sub-command help')
parser_create_sample.add_argument('-n', '--name', type=str, help='An optional string argument')
parser_create_sample.set_defaults(func=apm.createSampleTemplate)

args = parser.parse_args()

print("Argument values:")
print(args)
print(args.name)

args.func(args)
