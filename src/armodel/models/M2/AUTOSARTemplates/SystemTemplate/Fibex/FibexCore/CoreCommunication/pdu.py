"""Pdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 303)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 340)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    UnlimitedInteger,
)
from abc import ABC, abstractmethod


class Pdu(FibexElement, ABC):
    """AUTOSAR Pdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    has_dynamic: Optional[Boolean]
    length: Optional[UnlimitedInteger]
    def __init__(self) -> None:
        """Initialize Pdu."""
        super().__init__()
        self.has_dynamic: Optional[Boolean] = None
        self.length: Optional[UnlimitedInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize Pdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Pdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize has_dynamic
        if self.has_dynamic is not None:
            serialized = SerializationHelper.serialize_item(self.has_dynamic, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-DYNAMIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize length
        if self.length is not None:
            serialized = SerializationHelper.serialize_item(self.length, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Pdu":
        """Deserialize XML element to Pdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Pdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Pdu, cls).deserialize(element)

        # Parse has_dynamic
        child = SerializationHelper.find_child_element(element, "HAS-DYNAMIC")
        if child is not None:
            has_dynamic_value = child.text
            obj.has_dynamic = has_dynamic_value

        # Parse length
        child = SerializationHelper.find_child_element(element, "LENGTH")
        if child is not None:
            length_value = child.text
            obj.length = length_value

        return obj



class PduBuilder:
    """Builder for Pdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Pdu = Pdu()

    def build(self) -> Pdu:
        """Build and return Pdu object.

        Returns:
            Pdu instance
        """
        # TODO: Add validation
        return self._obj
