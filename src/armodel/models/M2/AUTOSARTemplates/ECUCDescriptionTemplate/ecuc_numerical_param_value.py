"""EcucNumericalParamValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 128)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 442)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class EcucNumericalParamValue(EcucParameterValue):
    """AUTOSAR EcucNumericalParamValue."""

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
        """Initialize EcucNumericalParamValue."""
        super().__init__()
        self.value: Optional[Numerical] = None


class EcucNumericalParamValueBuilder:
    """Builder for EcucNumericalParamValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucNumericalParamValue = EcucNumericalParamValue()

    def build(self) -> EcucNumericalParamValue:
        """Build and return EcucNumericalParamValue object.

        Returns:
            EcucNumericalParamValue instance
        """
        # TODO: Add validation
        return self._obj
