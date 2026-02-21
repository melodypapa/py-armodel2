"""Gateway AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 837)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.frame_mapping import (
    FrameMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_pdu_mapping import (
    IPduMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_signal_mapping import (
    ISignalMapping,
)


class Gateway(FibexElement):
    """AUTOSAR Gateway."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecu_ref: Optional[ARRef]
    frame_mapping_refs: list[ARRef]
    i_pdu_mapping_refs: list[ARRef]
    signal_mapping_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize Gateway."""
        super().__init__()
        self.ecu_ref: Optional[ARRef] = None
        self.frame_mapping_refs: list[ARRef] = []
        self.i_pdu_mapping_refs: list[ARRef] = []
        self.signal_mapping_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize Gateway to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Gateway, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecu_ref
        if self.ecu_ref is not None:
            serialized = ARObject._serialize_item(self.ecu_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize frame_mapping_refs (list to container "FRAME-MAPPING-REFS")
        if self.frame_mapping_refs:
            wrapper = ET.Element("FRAME-MAPPING-REFS")
            for item in self.frame_mapping_refs:
                serialized = ARObject._serialize_item(item, "FrameMapping")
                if serialized is not None:
                    child_elem = ET.Element("FRAME-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize i_pdu_mapping_refs (list to container "I-PDU-MAPPING-REFS")
        if self.i_pdu_mapping_refs:
            wrapper = ET.Element("I-PDU-MAPPING-REFS")
            for item in self.i_pdu_mapping_refs:
                serialized = ARObject._serialize_item(item, "IPduMapping")
                if serialized is not None:
                    child_elem = ET.Element("I-PDU-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize signal_mapping_refs (list to container "SIGNAL-MAPPING-REFS")
        if self.signal_mapping_refs:
            wrapper = ET.Element("SIGNAL-MAPPING-REFS")
            for item in self.signal_mapping_refs:
                serialized = ARObject._serialize_item(item, "ISignalMapping")
                if serialized is not None:
                    child_elem = ET.Element("SIGNAL-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Gateway":
        """Deserialize XML element to Gateway object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Gateway object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Gateway, cls).deserialize(element)

        # Parse ecu_ref
        child = ARObject._find_child_element(element, "ECU-REF")
        if child is not None:
            ecu_ref_value = ARRef.deserialize(child)
            obj.ecu_ref = ecu_ref_value

        # Parse frame_mapping_refs (list from container "FRAME-MAPPING-REFS")
        obj.frame_mapping_refs = []
        container = ARObject._find_child_element(element, "FRAME-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.frame_mapping_refs.append(child_value)

        # Parse i_pdu_mapping_refs (list from container "I-PDU-MAPPING-REFS")
        obj.i_pdu_mapping_refs = []
        container = ARObject._find_child_element(element, "I-PDU-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_pdu_mapping_refs.append(child_value)

        # Parse signal_mapping_refs (list from container "SIGNAL-MAPPING-REFS")
        obj.signal_mapping_refs = []
        container = ARObject._find_child_element(element, "SIGNAL-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.signal_mapping_refs.append(child_value)

        return obj



class GatewayBuilder:
    """Builder for Gateway."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Gateway = Gateway()

    def build(self) -> Gateway:
        """Build and return Gateway object.

        Returns:
            Gateway instance
        """
        # TODO: Add validation
        return self._obj
