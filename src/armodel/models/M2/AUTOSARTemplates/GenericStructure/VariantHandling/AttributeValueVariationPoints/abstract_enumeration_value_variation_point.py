"""AbstractEnumerationValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 421)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Ref,
)


class AbstractEnumerationValueVariationPoint(ARObject):
    """AUTOSAR AbstractEnumerationValueVariationPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # base
        "enum_table": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # enumTable
    }

    def __init__(self) -> None:
        """Initialize AbstractEnumerationValueVariationPoint."""
        super().__init__()
        self.base: Optional[Identifier] = None
        self.enum_table: Optional[Ref] = None


class AbstractEnumerationValueVariationPointBuilder:
    """Builder for AbstractEnumerationValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractEnumerationValueVariationPoint = AbstractEnumerationValueVariationPoint()

    def build(self) -> AbstractEnumerationValueVariationPoint:
        """Build and return AbstractEnumerationValueVariationPoint object.

        Returns:
            AbstractEnumerationValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
