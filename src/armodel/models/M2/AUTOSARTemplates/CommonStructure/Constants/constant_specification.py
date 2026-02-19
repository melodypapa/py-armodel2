"""ConstantSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class ConstantSpecification(ARElement):
    """AUTOSAR ConstantSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value_spec: Optional[ValueSpecification]
    def __init__(self) -> None:
        """Initialize ConstantSpecification."""
        super().__init__()
        self.value_spec: Optional[ValueSpecification] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantSpecification":
        """Deserialize XML element to ConstantSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConstantSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConstantSpecification, cls).deserialize(element)

        # Parse value_spec
        child = ARObject._find_child_element(element, "VALUE-SPEC")
        if child is not None:
            value_spec_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.value_spec = value_spec_value

        return obj



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
