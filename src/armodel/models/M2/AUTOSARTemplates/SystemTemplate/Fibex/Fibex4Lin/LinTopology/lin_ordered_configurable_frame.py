"""LinOrderedConfigurableFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)


class LinOrderedConfigurableFrame(ARObject):
    """AUTOSAR LinOrderedConfigurableFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    frame: Optional[LinFrame]
    index: Optional[Integer]
    def __init__(self) -> None:
        """Initialize LinOrderedConfigurableFrame."""
        super().__init__()
        self.frame: Optional[LinFrame] = None
        self.index: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinOrderedConfigurableFrame":
        """Deserialize XML element to LinOrderedConfigurableFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinOrderedConfigurableFrame object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse frame
        child = ARObject._find_child_element(element, "FRAME")
        if child is not None:
            frame_value = ARObject._deserialize_by_tag(child, "LinFrame")
            obj.frame = frame_value

        # Parse index
        child = ARObject._find_child_element(element, "INDEX")
        if child is not None:
            index_value = child.text
            obj.index = index_value

        return obj



class LinOrderedConfigurableFrameBuilder:
    """Builder for LinOrderedConfigurableFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinOrderedConfigurableFrame = LinOrderedConfigurableFrame()

    def build(self) -> LinOrderedConfigurableFrame:
        """Build and return LinOrderedConfigurableFrame object.

        Returns:
            LinOrderedConfigurableFrame instance
        """
        # TODO: Add validation
        return self._obj
