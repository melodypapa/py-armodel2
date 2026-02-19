"""EcucNumericalParamValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 128)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 442)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class EcucNumericalParamValue(EcucParameterValue):
    """AUTOSAR EcucNumericalParamValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize EcucNumericalParamValue."""
        super().__init__()
        self.value: Optional[Numerical] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucNumericalParamValue":
        """Deserialize XML element to EcucNumericalParamValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucNumericalParamValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



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
