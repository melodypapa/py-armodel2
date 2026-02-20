"""VariationRestrictionWithSeverity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class VariationRestrictionWithSeverity(RestrictionWithSeverity):
    """AUTOSAR VariationRestrictionWithSeverity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize VariationRestrictionWithSeverity."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize VariationRestrictionWithSeverity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VariationRestrictionWithSeverity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariationRestrictionWithSeverity":
        """Deserialize XML element to VariationRestrictionWithSeverity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariationRestrictionWithSeverity object
        """
        # Delegate to parent class to handle inherited attributes
        return super(VariationRestrictionWithSeverity, cls).deserialize(element)



class VariationRestrictionWithSeverityBuilder:
    """Builder for VariationRestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariationRestrictionWithSeverity = VariationRestrictionWithSeverity()

    def build(self) -> VariationRestrictionWithSeverity:
        """Build and return VariationRestrictionWithSeverity object.

        Returns:
            VariationRestrictionWithSeverity instance
        """
        # TODO: Add validation
        return self._obj
