"""Field AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 45)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_ApplicationDesign_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class Field(AutosarDataPrototype):
    """AUTOSAR Field."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    has_getter: Optional[Boolean]
    has_notifier: Optional[Boolean]
    has_setter: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize Field."""
        super().__init__()
        self.has_getter: Optional[Boolean] = None
        self.has_notifier: Optional[Boolean] = None
        self.has_setter: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize Field to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Field, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize has_getter
        if self.has_getter is not None:
            serialized = SerializationHelper.serialize_item(self.has_getter, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-GETTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize has_notifier
        if self.has_notifier is not None:
            serialized = SerializationHelper.serialize_item(self.has_notifier, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-NOTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize has_setter
        if self.has_setter is not None:
            serialized = SerializationHelper.serialize_item(self.has_setter, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-SETTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Field":
        """Deserialize XML element to Field object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Field object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Field, cls).deserialize(element)

        # Parse has_getter
        child = SerializationHelper.find_child_element(element, "HAS-GETTER")
        if child is not None:
            has_getter_value = child.text
            obj.has_getter = has_getter_value

        # Parse has_notifier
        child = SerializationHelper.find_child_element(element, "HAS-NOTIFIER")
        if child is not None:
            has_notifier_value = child.text
            obj.has_notifier = has_notifier_value

        # Parse has_setter
        child = SerializationHelper.find_child_element(element, "HAS-SETTER")
        if child is not None:
            has_setter_value = child.text
            obj.has_setter = has_setter_value

        return obj



class FieldBuilder:
    """Builder for Field."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Field = Field()

    def build(self) -> Field:
        """Build and return Field object.

        Returns:
            Field instance
        """
        # TODO: Add validation
        return self._obj
