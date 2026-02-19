"""CommConnectorPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 303)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class CommConnectorPort(Identifiable, ABC):
    """AUTOSAR CommConnectorPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication: Optional[Any]
    def __init__(self) -> None:
        """Initialize CommConnectorPort."""
        super().__init__()
        self.communication: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize CommConnectorPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommConnectorPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication
        if self.communication is not None:
            serialized = ARObject._serialize_item(self.communication, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommConnectorPort":
        """Deserialize XML element to CommConnectorPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommConnectorPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommConnectorPort, cls).deserialize(element)

        # Parse communication
        child = ARObject._find_child_element(element, "COMMUNICATION")
        if child is not None:
            communication_value = child.text
            obj.communication = communication_value

        return obj



class CommConnectorPortBuilder:
    """Builder for CommConnectorPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommConnectorPort = CommConnectorPort()

    def build(self) -> CommConnectorPort:
        """Build and return CommConnectorPort object.

        Returns:
            CommConnectorPort instance
        """
        # TODO: Add validation
        return self._obj
