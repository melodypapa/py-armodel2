"""SdgPrimitiveAttributeWithVariation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 101)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_primitive_attribute import (
    SdgAbstractPrimitiveAttribute,
)


class SdgPrimitiveAttributeWithVariation(SdgAbstractPrimitiveAttribute):
    """AUTOSAR SdgPrimitiveAttributeWithVariation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize SdgPrimitiveAttributeWithVariation."""
        super().__init__()


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
