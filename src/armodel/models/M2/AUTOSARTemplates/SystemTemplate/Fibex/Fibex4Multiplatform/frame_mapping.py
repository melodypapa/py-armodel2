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
    def serialize(self) -> ET.Element:
        """Serialize FrameMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize introduction
        if self.introduction is not None:
            serialized = ARObject._serialize_item(self.introduction, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTRODUCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_frame_ref
        if self.source_frame_ref is not None:
            serialized = ARObject._serialize_item(self.source_frame_ref, "FrameTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-FRAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_frame_ref
        if self.target_frame_ref is not None:
            serialized = ARObject._serialize_item(self.target_frame_ref, "FrameTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-FRAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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
