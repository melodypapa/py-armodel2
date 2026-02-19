"""NumericalValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 436)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2040)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class NumericalValueSpecification(ValueSpecification):
    """AUTOSAR NumericalValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize NumericalValueSpecification."""
        super().__init__()
        self.value: Optional[Numerical] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NumericalValueSpecification":
        """Deserialize XML element to NumericalValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NumericalValueSpecification object
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
