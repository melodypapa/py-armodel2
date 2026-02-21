"""SpecElementScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 84)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Common.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class SpecElementScope(SpecElementReference, ABC):
    """AUTOSAR SpecElementScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    in_scope: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize SpecElementScope."""
        super().__init__()
        self.in_scope: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize SpecElementScope to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SpecElementScope, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize in_scope
        if self.in_scope is not None:
            serialized = ARObject._serialize_item(self.in_scope, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IN-SCOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecElementScope":
        """Deserialize XML element to SpecElementScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SpecElementScope object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SpecElementScope, cls).deserialize(element)

        # Parse in_scope
        child = ARObject._find_child_element(element, "IN-SCOPE")
        if child is not None:
            in_scope_value = child.text
            obj.in_scope = in_scope_value

        return obj



class SpecElementScopeBuilder:
    """Builder for SpecElementScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecElementScope = SpecElementScope()

    def build(self) -> SpecElementScope:
        """Build and return SpecElementScope object.

        Returns:
            SpecElementScope instance
        """
        # TODO: Add validation
        return self._obj
