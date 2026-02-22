"""TDEventVfbPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 52)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
    TDEventVfb,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.Port.port_prototype_blueprint import (
    PortPrototypeBlueprint,
)
from abc import ABC, abstractmethod


class TDEventVfbPort(TDEventVfb, ABC):
    """AUTOSAR TDEventVfbPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    is_external: Optional[Boolean]
    port_ref: Optional[ARRef]
    port_prototype_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventVfbPort."""
        super().__init__()
        self.is_external: Optional[Boolean] = None
        self.port_ref: Optional[ARRef] = None
        self.port_prototype_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventVfbPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventVfbPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize is_external
        if self.is_external is not None:
            serialized = SerializationHelper.serialize_item(self.is_external, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-EXTERNAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize port_ref
        if self.port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize port_prototype_ref
        if self.port_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.port_prototype_ref, "PortPrototypeBlueprint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventVfbPort":
        """Deserialize XML element to TDEventVfbPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventVfbPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventVfbPort, cls).deserialize(element)

        # Parse is_external
        child = SerializationHelper.find_child_element(element, "IS-EXTERNAL")
        if child is not None:
            is_external_value = child.text
            obj.is_external = is_external_value

        # Parse port_ref
        child = SerializationHelper.find_child_element(element, "PORT-REF")
        if child is not None:
            port_ref_value = ARRef.deserialize(child)
            obj.port_ref = port_ref_value

        # Parse port_prototype_ref
        child = SerializationHelper.find_child_element(element, "PORT-PROTOTYPE-REF")
        if child is not None:
            port_prototype_ref_value = ARRef.deserialize(child)
            obj.port_prototype_ref = port_prototype_ref_value

        return obj



