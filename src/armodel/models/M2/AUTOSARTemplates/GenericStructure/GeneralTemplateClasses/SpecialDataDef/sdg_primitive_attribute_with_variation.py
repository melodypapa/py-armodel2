"""SdgPrimitiveAttributeWithVariation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 101)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_primitive_attribute import (
    SdgAbstractPrimitiveAttribute,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SdgPrimitiveAttributeWithVariation(SdgAbstractPrimitiveAttribute):
    """AUTOSAR SdgPrimitiveAttributeWithVariation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SdgPrimitiveAttributeWithVariation."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize SdgPrimitiveAttributeWithVariation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgPrimitiveAttributeWithVariation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgPrimitiveAttributeWithVariation":
        """Deserialize XML element to SdgPrimitiveAttributeWithVariation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgPrimitiveAttributeWithVariation object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SdgPrimitiveAttributeWithVariation, cls).deserialize(element)



class SdgPrimitiveAttributeWithVariationBuilder:
    """Builder for SdgPrimitiveAttributeWithVariation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgPrimitiveAttributeWithVariation = SdgPrimitiveAttributeWithVariation()

    def build(self) -> SdgPrimitiveAttributeWithVariation:
        """Build and return SdgPrimitiveAttributeWithVariation object.

        Returns:
            SdgPrimitiveAttributeWithVariation instance
        """
        # TODO: Add validation
        return self._obj
