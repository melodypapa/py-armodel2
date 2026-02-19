"""ConstantSpecificationMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)


class ConstantSpecificationMapping(ARObject):
    """AUTOSAR ConstantSpecificationMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    appl_constant: Optional[ConstantSpecification]
    impl_constant: Optional[ConstantSpecification]
    def __init__(self) -> None:
        """Initialize ConstantSpecificationMapping."""
        super().__init__()
        self.appl_constant: Optional[ConstantSpecification] = None
        self.impl_constant: Optional[ConstantSpecification] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantSpecificationMapping":
        """Deserialize XML element to ConstantSpecificationMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConstantSpecificationMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse appl_constant
        child = ARObject._find_child_element(element, "APPL-CONSTANT")
        if child is not None:
            appl_constant_value = ARObject._deserialize_by_tag(child, "ConstantSpecification")
            obj.appl_constant = appl_constant_value

        # Parse impl_constant
        child = ARObject._find_child_element(element, "IMPL-CONSTANT")
        if child is not None:
            impl_constant_value = ARObject._deserialize_by_tag(child, "ConstantSpecification")
            obj.impl_constant = impl_constant_value

        return obj



class ConstantSpecificationMappingBuilder:
    """Builder for ConstantSpecificationMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstantSpecificationMapping = ConstantSpecificationMapping()

    def build(self) -> ConstantSpecificationMapping:
        """Build and return ConstantSpecificationMapping object.

        Returns:
            ConstantSpecificationMapping instance
        """
        # TODO: Add validation
        return self._obj
