"""DdsResourceLimits AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 537)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsResourceLimits(ARObject):
    """AUTOSAR DdsResourceLimits."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_instances: Optional[PositiveInteger]
    max_samples: Optional[PositiveInteger]
    max_samples_per_instance: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DdsResourceLimits."""
        super().__init__()
        self.max_instances: Optional[PositiveInteger] = None
        self.max_samples: Optional[PositiveInteger] = None
        self.max_samples_per_instance: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsResourceLimits":
        """Deserialize XML element to DdsResourceLimits object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsResourceLimits object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse max_instances
        child = ARObject._find_child_element(element, "MAX-INSTANCES")
        if child is not None:
            max_instances_value = child.text
            obj.max_instances = max_instances_value

        # Parse max_samples
        child = ARObject._find_child_element(element, "MAX-SAMPLES")
        if child is not None:
            max_samples_value = child.text
            obj.max_samples = max_samples_value

        # Parse max_samples_per_instance
        child = ARObject._find_child_element(element, "MAX-SAMPLES-PER-INSTANCE")
        if child is not None:
            max_samples_per_instance_value = child.text
            obj.max_samples_per_instance = max_samples_per_instance_value

        return obj



class DdsResourceLimitsBuilder:
    """Builder for DdsResourceLimits."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsResourceLimits = DdsResourceLimits()

    def build(self) -> DdsResourceLimits:
        """Build and return DdsResourceLimits object.

        Returns:
            DdsResourceLimits instance
        """
        # TODO: Add validation
        return self._obj
