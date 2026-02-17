"""FMAttributeDef AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    Numerical,
)


class FMAttributeDef(Identifiable):
    """AUTOSAR FMAttributeDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "default_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # defaultValue
        "max": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # max
        "min": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # min
    }

    def __init__(self) -> None:
        """Initialize FMAttributeDef."""
        super().__init__()
        self.default_value: Optional[Numerical] = None
        self.max: Optional[Limit] = None
        self.min: Optional[Limit] = None


class FMAttributeDefBuilder:
    """Builder for FMAttributeDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMAttributeDef = FMAttributeDef()

    def build(self) -> FMAttributeDef:
        """Build and return FMAttributeDef object.

        Returns:
            FMAttributeDef instance
        """
        # TODO: Add validation
        return self._obj
