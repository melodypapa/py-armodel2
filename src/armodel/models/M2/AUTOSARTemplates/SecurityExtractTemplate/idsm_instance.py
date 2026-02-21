"""IdsmInstance AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.block_state import (
    BlockState,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.IntrusionDetectionSystem.idsm_module_instantiation import (
    IdsmModuleInstantiation,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_rate_limitation import (
    IdsmRateLimitation,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_traffic_limitation import (
    IdsmTrafficLimitation,
)


class IdsmInstance(IdsCommonElement):
    """AUTOSAR IdsmInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    block_states: list[BlockState]
    ecu_instance_ref: Optional[ARRef]
    idsm_instance_id: Optional[PositiveInteger]
    idsm_module_ref: Optional[ARRef]
    rate_limitation_ref: Optional[ARRef]
    signature: Optional[Any]
    timestamp: Optional[String]
    traffic_limitation_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize IdsmInstance."""
        super().__init__()
        self.block_states: list[BlockState] = []
        self.ecu_instance_ref: Optional[ARRef] = None
        self.idsm_instance_id: Optional[PositiveInteger] = None
        self.idsm_module_ref: Optional[ARRef] = None
        self.rate_limitation_ref: Optional[ARRef] = None
        self.signature: Optional[Any] = None
        self.timestamp: Optional[String] = None
        self.traffic_limitation_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize IdsmInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IdsmInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize block_states (list to container "BLOCK-STATES")
        if self.block_states:
            wrapper = ET.Element("BLOCK-STATES")
            for item in self.block_states:
                serialized = ARObject._serialize_item(item, "BlockState")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = ARObject._serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize idsm_instance_id
        if self.idsm_instance_id is not None:
            serialized = ARObject._serialize_item(self.idsm_instance_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDSM-INSTANCE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize idsm_module_ref
        if self.idsm_module_ref is not None:
            serialized = ARObject._serialize_item(self.idsm_module_ref, "IdsmModuleInstantiation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDSM-MODULE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_limitation_ref
        if self.rate_limitation_ref is not None:
            serialized = ARObject._serialize_item(self.rate_limitation_ref, "IdsmRateLimitation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-LIMITATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signature
        if self.signature is not None:
            serialized = ARObject._serialize_item(self.signature, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIGNATURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timestamp
        if self.timestamp is not None:
            serialized = ARObject._serialize_item(self.timestamp, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMESTAMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize traffic_limitation_ref
        if self.traffic_limitation_ref is not None:
            serialized = ARObject._serialize_item(self.traffic_limitation_ref, "IdsmTrafficLimitation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRAFFIC-LIMITATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmInstance":
        """Deserialize XML element to IdsmInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IdsmInstance, cls).deserialize(element)

        # Parse block_states (list from container "BLOCK-STATES")
        obj.block_states = []
        container = ARObject._find_child_element(element, "BLOCK-STATES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.block_states.append(child_value)

        # Parse ecu_instance_ref
        child = ARObject._find_child_element(element, "ECU-INSTANCE-REF")
        if child is not None:
            ecu_instance_ref_value = ARRef.deserialize(child)
            obj.ecu_instance_ref = ecu_instance_ref_value

        # Parse idsm_instance_id
        child = ARObject._find_child_element(element, "IDSM-INSTANCE-ID")
        if child is not None:
            idsm_instance_id_value = child.text
            obj.idsm_instance_id = idsm_instance_id_value

        # Parse idsm_module_ref
        child = ARObject._find_child_element(element, "IDSM-MODULE-REF")
        if child is not None:
            idsm_module_ref_value = ARRef.deserialize(child)
            obj.idsm_module_ref = idsm_module_ref_value

        # Parse rate_limitation_ref
        child = ARObject._find_child_element(element, "RATE-LIMITATION-REF")
        if child is not None:
            rate_limitation_ref_value = ARRef.deserialize(child)
            obj.rate_limitation_ref = rate_limitation_ref_value

        # Parse signature
        child = ARObject._find_child_element(element, "SIGNATURE")
        if child is not None:
            signature_value = child.text
            obj.signature = signature_value

        # Parse timestamp
        child = ARObject._find_child_element(element, "TIMESTAMP")
        if child is not None:
            timestamp_value = child.text
            obj.timestamp = timestamp_value

        # Parse traffic_limitation_ref
        child = ARObject._find_child_element(element, "TRAFFIC-LIMITATION-REF")
        if child is not None:
            traffic_limitation_ref_value = ARRef.deserialize(child)
            obj.traffic_limitation_ref = traffic_limitation_ref_value

        return obj



class IdsmInstanceBuilder:
    """Builder for IdsmInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmInstance = IdsmInstance()

    def build(self) -> IdsmInstance:
        """Build and return IdsmInstance object.

        Returns:
            IdsmInstance instance
        """
        # TODO: Add validation
        return self._obj
