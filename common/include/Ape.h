/*MIT License

Copyright (c) 2016 MTA SZTAKI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*/

#ifndef APE_H
#define APE_H

#include <vector>
#include <string>
#include <map>
#include <memory>

namespace Ape
{	
	class INode;

	typedef std::shared_ptr<INode> NodeSharedPtr;

	typedef std::weak_ptr<INode> NodeWeakPtr;

	typedef std::vector<NodeSharedPtr> NodeSharedPtrVector;

	typedef std::vector<NodeWeakPtr> NodeWeakPtrVector;

	typedef std::map<std::string, NodeWeakPtr> NodeWeakPtrNameMap;

	typedef std::map<std::string, NodeSharedPtr> NodeSharedPtrNameMap;

	class Geometry;
	
	typedef std::weak_ptr<Geometry> GeometryWeakPtr;

	class ILight;

	typedef std::weak_ptr<ILight> LightWeakPtr;

	class Entity;

	typedef std::shared_ptr<Entity> EntitySharedPtr;

	typedef std::weak_ptr<Entity> EntityWeakPtr;

	typedef std::vector<EntitySharedPtr> EntitySharedPtrVector;

	typedef std::vector<EntityWeakPtr> EntityWeakPtrVector;

	typedef std::map<std::string, EntityWeakPtr> EntityWeakPtrNameMap;

	typedef std::map<std::string, EntitySharedPtr> EntitySharedPtrNameMap;

	class Geometry;

	typedef std::weak_ptr<Geometry> GeometryWeakPtr;

	class SubGeometry;

	class Pass;

	typedef std::weak_ptr<Pass> PassWeakPtr;

	class Material;

	typedef std::weak_ptr<Material> MaterialWeakPtr;
}

#endif
