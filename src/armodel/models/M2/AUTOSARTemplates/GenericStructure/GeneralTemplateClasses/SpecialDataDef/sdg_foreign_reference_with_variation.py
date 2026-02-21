"""SdgForeignReferenceWithVariation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_foreign_reference import (
    SdgAbstractForeignReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SdgForeignReferenceWithVariation(SdgAbstractForeignReference):
    """AUTOSAR SdgForeignReferenceWithVariation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SdgForeignReferenceWithVariation."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SdgForeignReferenceWithVariation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgForeignReferenceWithVariation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgForeignReferenceWithVariation":
        """Deserialize XML element to SdgForeignReferenceWithVariation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgForeignReferenceWithVariation object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SdgForeignReferenceWithVariation, cls).deserialize(element)



class SdgForeignReferenceWithVariationBuilder:
    """Builder for SdgForeignReferenceWithVariation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgForeignReferenceWithVariation = SdgForeignReferenceWithVariation()

    def build(self) -> SdgForeignReferenceWithVariation:
        """Build and return SdgForeignReferenceWithVariation object.

        Returns:
            SdgForeignReferenceWithVariation instance
        """
        # TODO: Add validation
        return self._obj
