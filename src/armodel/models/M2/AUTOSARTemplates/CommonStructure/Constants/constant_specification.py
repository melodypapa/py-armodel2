"""ConstantSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class ConstantSpecification(ARElement):
    """AUTOSAR ConstantSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "value_spec": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # valueSpec
    }

    def __init__(self) -> None:
        """Initialize ConstantSpecification."""
        super().__init__()
        self.value_spec: Optional[ValueSpecification] = None


class ConstantSpecificationBuilder:
    """Builder for ConstantSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstantSpecification = ConstantSpecification()

    def build(self) -> ConstantSpecification:
        """Build and return ConstantSpecification object.

        Returns:
            ConstantSpecification instance
        """
        # TODO: Add validation
        return self._obj
