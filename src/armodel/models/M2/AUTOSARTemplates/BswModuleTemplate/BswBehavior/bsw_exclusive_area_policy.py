"""BswExclusiveAreaPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ApiPrincipleEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)


class BswExclusiveAreaPolicy(ARObject):
    """AUTOSAR BswExclusiveAreaPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    api_principle_enum: Optional[ApiPrincipleEnum]
    exclusive_area: Optional[ExclusiveArea]
    def __init__(self) -> None:
        """Initialize BswExclusiveAreaPolicy."""
        super().__init__()
        self.api_principle_enum: Optional[ApiPrincipleEnum] = None
        self.exclusive_area: Optional[ExclusiveArea] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswExclusiveAreaPolicy":
        """Deserialize XML element to BswExclusiveAreaPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswExclusiveAreaPolicy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse api_principle_enum
        child = ARObject._find_child_element(element, "API-PRINCIPLE-ENUM")
        if child is not None:
            api_principle_enum_value = child.text
            obj.api_principle_enum = api_principle_enum_value

        # Parse exclusive_area
        child = ARObject._find_child_element(element, "EXCLUSIVE-AREA")
        if child is not None:
            exclusive_area_value = ARObject._deserialize_by_tag(child, "ExclusiveArea")
            obj.exclusive_area = exclusive_area_value

        return obj



class BswExclusiveAreaPolicyBuilder:
    """Builder for BswExclusiveAreaPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswExclusiveAreaPolicy = BswExclusiveAreaPolicy()

    def build(self) -> BswExclusiveAreaPolicy:
        """Build and return BswExclusiveAreaPolicy object.

        Returns:
            BswExclusiveAreaPolicy instance
        """
        # TODO: Add validation
        return self._obj
