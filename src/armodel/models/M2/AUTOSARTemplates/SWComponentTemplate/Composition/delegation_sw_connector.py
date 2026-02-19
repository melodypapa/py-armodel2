"""DelegationSwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2016)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class DelegationSwConnector(SwConnector):
    """AUTOSAR DelegationSwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    inner_port_instance_ref: Optional[ARRef]
    outer_port_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DelegationSwConnector."""
        super().__init__()
        self.inner_port_instance_ref: Optional[ARRef] = None
        self.outer_port_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize DelegationSwConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DelegationSwConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize inner_port_instance_ref
        if self.inner_port_instance_ref is not None:
            serialized = ARObject._serialize_item(self.inner_port_instance_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INNER-PORT-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize outer_port_ref
        if self.outer_port_ref is not None:
            serialized = ARObject._serialize_item(self.outer_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OUTER-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DelegationSwConnector":
        """Deserialize XML element to DelegationSwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DelegationSwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DelegationSwConnector, cls).deserialize(element)

        # Parse inner_port_instance_ref
        child = ARObject._find_child_element(element, "INNER-PORT-INSTANCE-REF")
        if child is not None:
            inner_port_instance_ref_value = ARRef.deserialize(child)
            obj.inner_port_instance_ref = inner_port_instance_ref_value

        # Parse outer_port_ref
        child = ARObject._find_child_element(element, "OUTER-PORT-REF")
        if child is not None:
            outer_port_ref_value = ARRef.deserialize(child)
            obj.outer_port_ref = outer_port_ref_value

        return obj



class DelegationSwConnectorBuilder:
    """Builder for DelegationSwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DelegationSwConnector = DelegationSwConnector()

    def build(self) -> DelegationSwConnector:
        """Build and return DelegationSwConnector object.

        Returns:
            DelegationSwConnector instance
        """
        # TODO: Add validation
        return self._obj
