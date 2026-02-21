"""ISignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 846)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)


class ISignalMapping(ARObject):
    """AUTOSAR ISignalMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    introduction: Optional[DocumentationBlock]
    source_signal_ref: Optional[ARRef]
    target_signal_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ISignalMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
        self.source_signal_ref: Optional[ARRef] = None
        self.target_signal_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ISignalMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignalMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize introduction
        if self.introduction is not None:
            serialized = SerializationHelper.serialize_item(self.introduction, "DocumentationBlock")
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

        # Serialize source_signal_ref
        if self.source_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.source_signal_ref, "ISignalTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_signal_ref
        if self.target_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_signal_ref, "ISignalTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalMapping":
        """Deserialize XML element to ISignalMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalMapping, cls).deserialize(element)

        # Parse introduction
        child = SerializationHelper.find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        # Parse source_signal_ref
        child = SerializationHelper.find_child_element(element, "SOURCE-SIGNAL-REF")
        if child is not None:
            source_signal_ref_value = ARRef.deserialize(child)
            obj.source_signal_ref = source_signal_ref_value

        # Parse target_signal_ref
        child = SerializationHelper.find_child_element(element, "TARGET-SIGNAL-REF")
        if child is not None:
            target_signal_ref_value = ARRef.deserialize(child)
            obj.target_signal_ref = target_signal_ref_value

        return obj



class ISignalMappingBuilder:
    """Builder for ISignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalMapping = ISignalMapping()

    def build(self) -> ISignalMapping:
        """Build and return ISignalMapping object.

        Returns:
            ISignalMapping instance
        """
        # TODO: Add validation
        return self._obj
