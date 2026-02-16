"""
Reflection-based serialization strategy.

This module implements the default serialization strategy that uses
reflection and XMLMember metadata to serialize and deserialize
AUTOSAR model objects.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import TYPE_CHECKING, Any

from armodel.serialization.base import (
    DeserializationContext,
    SerializationContext,
    SerializationStrategy,
)

if TYPE_CHECKING:
    from armodel.serialization.metadata import XMLMember


class ReflectionSerializer(SerializationStrategy):
    """
    Default serialization strategy using reflection and metadata.

    This strategy handles most AUTOSAR model classes by:
    1. Extracting XML metadata via get_xml_metadata()
    2. Using reflection to get/set instance attributes
    3. Recursively serializing child elements
    """

    def can_handle(self, obj: type | object) -> bool:
        """
        Check if this strategy can handle the given object.

        This strategy can handle any object with _xml_members metadata.

        Args:
            obj: The object or class to check

        Returns:
            True if the object has _xml_members metadata
        """
        cls = obj if isinstance(obj, type) else type(obj)
        return hasattr(cls, "_xml_members")

    def serialize(
        self,
        obj: object,
        context: SerializationContext,
        element: ET.Element | None = None,
    ) -> ET.Element:
        """
        Serialize an object to XML.

        Args:
            obj: The object to serialize
            context: Serialization context
            element: Optional existing element to serialize into

        Returns:
            The XML element representing the object
        """
        # Import here to avoid circular import
        from armodel.serialization.metadata import get_xml_metadata

        cls = type(obj)
        metadata = get_xml_metadata(cls)

        # Create or get element
        if element is None:
            # Determine tag name from class
            tag = self._get_class_xml_tag(cls)
            element = ET.Element(tag)

        # Set namespace if provided
        if context.namespace:
            # For lxml compatibility, we'll handle namespaces via attributes
            if element.tag.startswith("{"):
                # Already has namespace
                pass
            else:
                # Add namespace to tag
                element.tag = f"{{{context.namespace}}}{element.tag}"

        # Serialize each member
        for member_name, member_meta in metadata.items():
            if not hasattr(obj, member_name):
                continue

            value = getattr(obj, member_name)

            # Skip None values for optional members
            if value is None and not member_meta.is_required():
                continue

            # Serialize based on member type
            if member_meta.is_attribute:
                self._serialize_attribute(element, member_meta, value)
            elif member_meta.is_list():
                self._serialize_list(obj, element, member_meta, value, context)
            else:
                self._serialize_single_element(obj, element, member_meta, value, context)

        return element

    def _get_class_xml_tag(self, cls: type) -> str:
        """
        Get the XML tag name for a class.

        Args:
            cls: The class to get the tag for

        Returns:
            XML tag name
        """
        # Try to get tag from class name
        # Just uppercase the class name - don't insert hyphens
        name = cls.__name__

        # Handle special cases - these keep their exact names
        if name in ("AUTOSAR", "ARObject", "ARPACKAGE"):
            return name.upper()

        # For most classes, just uppercase
        # This matches the legacy behavior
        return name.upper()

    def _serialize_attribute(
        self,
        element: ET.Element,
        member_meta: XMLMember,
        value: Any,
    ) -> None:
        """
        Serialize an attribute.

        Args:
            element: The XML element
            member_meta: Member metadata
            value: The attribute value
        """
        if value is None:
            return

        tag = member_meta.get_xml_tag()
        element.set(tag, str(value))

    def _serialize_list(
        self,
        obj: object,
        element: ET.Element,
        member_meta: XMLMember,
        value: list[Any],
        context: SerializationContext,
    ) -> None:
        """
        Serialize a list member.

        Args:
            obj: The parent object
            element: The XML element
            member_meta: Member metadata
            value: The list value
            context: Serialization context
        """
        if not value:
            return

        tag = member_meta.get_xml_tag()

        for item in value:
            if member_meta.element_class and hasattr(item, "serialize"):
                # Recursively serialize child objects
                child_element = item.serialize(context.namespace)
                element.append(child_element)
            else:
                # Primitive type - create element with text content
                child_element = ET.Element(tag)
                child_element.text = str(item) if item is not None else None
                element.append(child_element)

    def _serialize_single_element(
        self,
        obj: object,
        element: ET.Element,
        member_meta: XMLMember,
        value: Any,
        context: SerializationContext,
    ) -> None:
        """
        Serialize a single element member.

        Args:
            obj: The parent object
            element: The XML element
            member_meta: Member metadata
            value: The element value
            context: Serialization context
        """
        if value is None:
            return

        tag = member_meta.get_xml_tag()

        if member_meta.element_class and hasattr(value, "serialize"):
            # Recursively serialize child object
            child_element = value.serialize(context.namespace)
            element.append(child_element)
        else:
            # Primitive type - create element with text content
            child_element = ET.Element(tag)
            child_element.text = str(value)
            element.append(child_element)

    def deserialize(
        self,
        cls: type,
        element: ET.Element,
        context: DeserializationContext,
    ) -> object:
        """
        Deserialize an object from XML.

        Args:
            cls: The class to instantiate
            element: The XML element to deserialize from
            context: Deserialization context

        Returns:
            The deserialized object
        """
        # Import here to avoid circular import
        from armodel.serialization.metadata import get_xml_metadata

        # Create instance
        instance = cls.__new__(cls)  # type: ignore[call-overload]

        # Call __init__ first to set default values
        # This must be done BEFORE we set attributes from XML
        if hasattr(instance, "__init__"):
            try:
                instance.__init__()
            except Exception:
                # Some classes have required __init__ arguments
                pass

        # Get metadata
        metadata = get_xml_metadata(cls)

        # Initialize each member from XML (overriding defaults)
        for member_name, member_meta in metadata.items():
            if member_meta.is_attribute:
                value = self._deserialize_attribute(element, member_meta)
            elif member_meta.is_list():
                value = self._deserialize_list(element, member_meta, context)
            else:
                value = self._deserialize_single_element(element, member_meta, context)

            # Set the attribute (override __init__ default)
            setattr(instance, member_name, value)

        return instance

    def _deserialize_attribute(
        self,
        element: ET.Element,
        member_meta: XMLMember,
    ) -> Any:
        """
        Deserialize an attribute.

        Args:
            element: The XML element
            member_meta: Member metadata

        Returns:
            The attribute value
        """
        tag = member_meta.get_xml_tag()
        value = element.get(tag)

        if value is None:
            return None

        # Convert to appropriate type based on element_class
        if member_meta.element_class:
            # For now, return as string - type conversion happens later
            return value

        return value

    def _deserialize_list(
        self,
        element: ET.Element,
        member_meta: XMLMember,
        context: DeserializationContext,
    ) -> list[Any]:
        """
        Deserialize a list member.

        Args:
            element: The XML element
            member_meta: Member metadata
            context: Deserialization context

        Returns:
            The list of values
        """
        if not member_meta.element_class:
            return []

        tag = member_meta.get_xml_tag()
        items = []

        # Find all matching child elements
        for child in element:
            # Check if this child matches our tag
            child_tag = child.tag
            if "{" in child_tag:
                # Strip namespace
                child_tag = child_tag.split("}", 1)[1]

            if child_tag == tag:
                # Deserialize child element
                item = self._deserialize_child_element(child, member_meta, context)
                if item is not None:
                    items.append(item)

        return items

    def _deserialize_single_element(
        self,
        element: ET.Element,
        member_meta: XMLMember,
        context: DeserializationContext,
    ) -> Any:
        """
        Deserialize a single element member.

        Args:
            element: The XML element
            member_meta: Member metadata
            context: Deserialization context

        Returns:
            The element value
        """
        if not member_meta.element_class:
            return None

        tag = member_meta.get_xml_tag()

        # Find the matching child element
        for child in element:
            child_tag = child.tag
            if "{" in child_tag:
                # Strip namespace
                child_tag = child_tag.split("}", 1)[1]

            if child_tag == tag:
                return self._deserialize_child_element(child, member_meta, context)

        return None

    def _deserialize_child_element(
        self,
        child: ET.Element,
        member_meta: XMLMember,
        context: DeserializationContext,
    ) -> Any:
        """
        Deserialize a child element.

        Args:
            child: The child XML element
            member_meta: Member metadata
            context: Deserialization context

        Returns:
            The deserialized value
        """
        if member_meta.element_class is None:
            # Primitive type - return text content
            return child.text if child.text else None

        # Check if the class has a deserialize method
        if hasattr(member_meta.element_class, "deserialize"):
            return member_meta.element_class.deserialize(child)

        # Fall back to using this strategy recursively
        return self.deserialize(member_meta.element_class, child, context)
