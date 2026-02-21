"""RTriggerInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 945)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.trigger_in_atomic_swc_instance_ref import (
    TriggerInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class RTriggerInAtomicSwcInstanceRef(TriggerInAtomicSwcInstanceRef):
    """AUTOSAR RTriggerInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_r_port_prototype_ref: Optional[ARRef]
    target_trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RTriggerInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_r_port_prototype_ref: Optional[ARRef] = None
        self.target_trigger_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RTriggerInAtomicSwcInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RTriggerInAtomicSwcInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_r_port_prototype_ref
        if self.context_r_port_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_r_port_prototype_ref, "AbstractRequiredPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-R-PORT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_trigger_ref
        if self.target_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RTriggerInAtomicSwcInstanceRef":
        """Deserialize XML element to RTriggerInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RTriggerInAtomicSwcInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RTriggerInAtomicSwcInstanceRef, cls).deserialize(element)

        # Parse context_r_port_prototype_ref
        child = SerializationHelper.find_child_element(element, "CONTEXT-R-PORT-PROTOTYPE-REF")
        if child is not None:
            context_r_port_prototype_ref_value = ARRef.deserialize(child)
            obj.context_r_port_prototype_ref = context_r_port_prototype_ref_value

        # Parse target_trigger_ref
        child = SerializationHelper.find_child_element(element, "TARGET-TRIGGER-REF")
        if child is not None:
            target_trigger_ref_value = ARRef.deserialize(child)
            obj.target_trigger_ref = target_trigger_ref_value

        return obj



class RTriggerInAtomicSwcInstanceRefBuilder:
    """Builder for RTriggerInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RTriggerInAtomicSwcInstanceRef = RTriggerInAtomicSwcInstanceRef()

    def build(self) -> RTriggerInAtomicSwcInstanceRef:
        """Build and return RTriggerInAtomicSwcInstanceRef object.

        Returns:
            RTriggerInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
