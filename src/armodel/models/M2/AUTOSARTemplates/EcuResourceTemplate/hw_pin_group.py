"""HwPinGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 19)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2027)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group_content import (
        HwPinGroupContent,
    )



class HwPinGroup(Identifiable):
    """AUTOSAR HwPinGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_pin_group_content_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize HwPinGroup."""
        super().__init__()
        self.hw_pin_group_content_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPinGroup":
        """Deserialize XML element to HwPinGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPinGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwPinGroup, cls).deserialize(element)

        # Parse hw_pin_group_content_ref
        child = ARObject._find_child_element(element, "HW-PIN-GROUP-CONTENT")
        if child is not None:
            hw_pin_group_content_ref_value = ARObject._deserialize_by_tag(child, "HwPinGroupContent")
            obj.hw_pin_group_content_ref = hw_pin_group_content_ref_value

        return obj



class HwPinGroupBuilder:
    """Builder for HwPinGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinGroup = HwPinGroup()

    def build(self) -> HwPinGroup:
        """Build and return HwPinGroup object.

        Returns:
            HwPinGroup instance
        """
        # TODO: Add validation
        return self._obj
