"""EcucIntegerParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 60)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UnlimitedInteger,
)


class EcucIntegerParamDef(EcucParameterDef):
    """AUTOSAR EcucIntegerParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_value: Optional[UnlimitedInteger]
    max: Optional[UnlimitedInteger]
    min: Optional[UnlimitedInteger]
    def __init__(self) -> None:
        """Initialize EcucIntegerParamDef."""
        super().__init__()
        self.default_value: Optional[UnlimitedInteger] = None
        self.max: Optional[UnlimitedInteger] = None
        self.min: Optional[UnlimitedInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucIntegerParamDef":
        """Deserialize XML element to EcucIntegerParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucIntegerParamDef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse default_value
        child = ARObject._find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = child.text
            obj.default_value = default_value_value

        # Parse max
        child = ARObject._find_child_element(element, "MAX")
        if child is not None:
            max_value = child.text
            obj.max = max_value

        # Parse min
        child = ARObject._find_child_element(element, "MIN")
        if child is not None:
            min_value = child.text
            obj.min = min_value

        return obj



class EcucIntegerParamDefBuilder:
    """Builder for EcucIntegerParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucIntegerParamDef = EcucIntegerParamDef()

    def build(self) -> EcucIntegerParamDef:
        """Build and return EcucIntegerParamDef object.

        Returns:
            EcucIntegerParamDef instance
        """
        # TODO: Add validation
        return self._obj
