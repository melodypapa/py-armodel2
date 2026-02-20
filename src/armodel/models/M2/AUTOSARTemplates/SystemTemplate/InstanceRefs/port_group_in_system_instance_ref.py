"""PortGroupInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1007)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class PortGroupInSystemInstanceRef(ARObject):
    """AUTOSAR PortGroupInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_ref: Optional[ARRef]
    context_ref: Optional[ARRef]
    target_ref: ARRef
    def __init__(self) -> None:
        """Initialize PortGroupInSystemInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_ref: Optional[ARRef] = None
        self.target_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize PortGroupInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = ARObject._serialize_item(self.base_ref, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_ref
        if self.context_ref is not None:
            serialized = ARObject._serialize_item(self.context_ref, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_ref
        if self.target_ref is not None:
            serialized = ARObject._serialize_item(self.target_ref, "PortGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortGroupInSystemInstanceRef":
        """Deserialize XML element to PortGroupInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortGroupInSystemInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base_ref
        child = ARObject._find_child_element(element, "BASE-REF")
        if child is not None:
            base_ref_value = ARRef.deserialize(child)
            obj.base_ref = base_ref_value

        # Parse context_ref
        child = ARObject._find_child_element(element, "CONTEXT-REF")
        if child is not None:
            context_ref_value = ARRef.deserialize(child)
            obj.context_ref = context_ref_value

        # Parse target_ref
        child = ARObject._find_child_element(element, "TARGET-REF")
        if child is not None:
            target_ref_value = ARRef.deserialize(child)
            obj.target_ref = target_ref_value

        return obj



class PortGroupInSystemInstanceRefBuilder:
    """Builder for PortGroupInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortGroupInSystemInstanceRef = PortGroupInSystemInstanceRef()

    def build(self) -> PortGroupInSystemInstanceRef:
        """Build and return PortGroupInSystemInstanceRef object.

        Returns:
            PortGroupInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
