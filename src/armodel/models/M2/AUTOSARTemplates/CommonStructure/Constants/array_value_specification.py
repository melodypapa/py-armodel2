"""ArrayValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 303)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 434)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1999)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class ArrayValueSpecification(CompositeValueSpecification):
    """AUTOSAR ArrayValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    elements: list[ValueSpecification]
    intended_partial: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ArrayValueSpecification."""
        super().__init__()
        self.elements: list[ValueSpecification] = []
        self.intended_partial: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArrayValueSpecification":
        """Deserialize XML element to ArrayValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArrayValueSpecification object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse elements (list)
        obj.elements = []
        for child in ARObject._find_all_child_elements(element, "ELEMENTS"):
            elements_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.elements.append(elements_value)

        # Parse intended_partial
        child = ARObject._find_child_element(element, "INTENDED-PARTIAL")
        if child is not None:
            intended_partial_value = child.text
            obj.intended_partial = intended_partial_value

        return obj



class ArrayValueSpecificationBuilder:
    """Builder for ArrayValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArrayValueSpecification = ArrayValueSpecification()

    def build(self) -> ArrayValueSpecification:
        """Build and return ArrayValueSpecification object.

        Returns:
            ArrayValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
