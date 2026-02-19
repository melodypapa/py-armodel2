"""FrameMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 838)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)


class FrameMapping(ARObject):
    """AUTOSAR FrameMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    introduction: Optional[DocumentationBlock]
    source_frame_ref: Optional[ARRef]
    target_frame_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize FrameMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
        self.source_frame_ref: Optional[ARRef] = None
        self.target_frame_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FrameMapping":
        """Deserialize XML element to FrameMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FrameMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse introduction
        child = ARObject._find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        # Parse source_frame_ref
        child = ARObject._find_child_element(element, "SOURCE-FRAME")
        if child is not None:
            source_frame_ref_value = ARObject._deserialize_by_tag(child, "FrameTriggering")
            obj.source_frame_ref = source_frame_ref_value

        # Parse target_frame_ref
        child = ARObject._find_child_element(element, "TARGET-FRAME")
        if child is not None:
            target_frame_ref_value = ARObject._deserialize_by_tag(child, "FrameTriggering")
            obj.target_frame_ref = target_frame_ref_value

        return obj



class FrameMappingBuilder:
    """Builder for FrameMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FrameMapping = FrameMapping()

    def build(self) -> FrameMapping:
        """Build and return FrameMapping object.

        Returns:
            FrameMapping instance
        """
        # TODO: Add validation
        return self._obj
