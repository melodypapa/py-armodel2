"""RestrictionWithSeverity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 86)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Common.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint import (
    SeverityEnum,
)
from abc import ABC, abstractmethod


class RestrictionWithSeverity(ARObject, ABC):
    """AUTOSAR RestrictionWithSeverity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    severity: SeverityEnum
    def __init__(self) -> None:
        """Initialize RestrictionWithSeverity."""
        super().__init__()
        self.severity: SeverityEnum = None

    def serialize(self) -> ET.Element:
        """Serialize RestrictionWithSeverity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RestrictionWithSeverity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize severity
        if self.severity is not None:
            serialized = SerializationHelper.serialize_item(self.severity, "SeverityEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEVERITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RestrictionWithSeverity":
        """Deserialize XML element to RestrictionWithSeverity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RestrictionWithSeverity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RestrictionWithSeverity, cls).deserialize(element)

        # Parse severity
        child = SerializationHelper.find_child_element(element, "SEVERITY")
        if child is not None:
            severity_value = SeverityEnum.deserialize(child)
            obj.severity = severity_value

        return obj



class RestrictionWithSeverityBuilder:
    """Builder for RestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RestrictionWithSeverity = RestrictionWithSeverity()

    def build(self) -> RestrictionWithSeverity:
        """Build and return RestrictionWithSeverity object.

        Returns:
            RestrictionWithSeverity instance
        """
        # TODO: Add validation
        return self._obj
