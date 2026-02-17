"""NumericalValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 436)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2040)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class NumericalValueSpecification(ValueSpecification):
    """AUTOSAR NumericalValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize NumericalValueSpecification."""
        super().__init__()
        self.value: Optional[Numerical] = None


class NumericalValueSpecificationBuilder:
    """Builder for NumericalValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NumericalValueSpecification = NumericalValueSpecification()

    def build(self) -> NumericalValueSpecification:
        """Build and return NumericalValueSpecification object.

        Returns:
            NumericalValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
