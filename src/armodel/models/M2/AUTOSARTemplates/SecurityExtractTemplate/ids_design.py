"""IdsDesign AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 16)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)


class IdsDesign(ARElement):
    """AUTOSAR IdsDesign."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=IdsCommonElement,
        ),  # elements
    }

    def __init__(self) -> None:
        """Initialize IdsDesign."""
        super().__init__()
        self.elements: list[IdsCommonElement] = []


class IdsDesignBuilder:
    """Builder for IdsDesign."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsDesign = IdsDesign()

    def build(self) -> IdsDesign:
        """Build and return IdsDesign object.

        Returns:
            IdsDesign instance
        """
        # TODO: Add validation
        return self._obj
