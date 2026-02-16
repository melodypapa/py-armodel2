"""PredefinedVariant AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.predefined_variant import (
    PredefinedVariant,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)


class PredefinedVariant(ARElement):
    """AUTOSAR PredefinedVariant."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "included_variants": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PredefinedVariant,
        ),  # includedVariants
        "post_build_variants": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (PostBuildVariant),
        ),  # postBuildVariants
        "sws": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwSystemconstantValueSet,
        ),  # sws
    }

    def __init__(self) -> None:
        """Initialize PredefinedVariant."""
        super().__init__()
        self.included_variants: list[PredefinedVariant] = []
        self.post_build_variants: list[Any] = []
        self.sws: list[SwSystemconstantValueSet] = []


class PredefinedVariantBuilder:
    """Builder for PredefinedVariant."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PredefinedVariant = PredefinedVariant()

    def build(self) -> PredefinedVariant:
        """Build and return PredefinedVariant object.

        Returns:
            PredefinedVariant instance
        """
        # TODO: Add validation
        return self._obj
