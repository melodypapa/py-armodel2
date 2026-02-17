"""AliasNameSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 174)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 968)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.alias_name_assignment import (
    AliasNameAssignment,
)


class AliasNameSet(ARElement):
    """AUTOSAR AliasNameSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "alias_names": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AliasNameAssignment,
        ),  # aliasNames
    }

    def __init__(self) -> None:
        """Initialize AliasNameSet."""
        super().__init__()
        self.alias_names: list[AliasNameAssignment] = []


class AliasNameSetBuilder:
    """Builder for AliasNameSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AliasNameSet = AliasNameSet()

    def build(self) -> AliasNameSet:
        """Build and return AliasNameSet object.

        Returns:
            AliasNameSet instance
        """
        # TODO: Add validation
        return self._obj
