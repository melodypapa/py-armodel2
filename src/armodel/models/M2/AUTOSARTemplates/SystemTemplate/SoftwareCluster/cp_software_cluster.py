"""CpSoftwareCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 309)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 893)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 221)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)


class CpSoftwareCluster(ARElement):
    """AUTOSAR CpSoftwareCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    software_cluster: Optional[PositiveInteger]
    sw_components: list[Any]
    sw_composition_component_type_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize CpSoftwareCluster."""
        super().__init__()
        self.software_cluster: Optional[PositiveInteger] = None
        self.sw_components: list[Any] = []
        self.sw_composition_component_type_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize software_cluster
        if self.software_cluster is not None:
            serialized = SerializationHelper.serialize_item(self.software_cluster, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE-CLUSTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_components (list to container "SW-COMPONENTS")
        if self.sw_components:
            wrapper = ET.Element("SW-COMPONENTS")
            for item in self.sw_components:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_composition_component_type_refs (list to container "SW-COMPOSITION-COMPONENT-TYPE-REFS")
        if self.sw_composition_component_type_refs:
            wrapper = ET.Element("SW-COMPOSITION-COMPONENT-TYPE-REFS")
            for item in self.sw_composition_component_type_refs:
                serialized = SerializationHelper.serialize_item(item, "CompositionSwComponentType")
                if serialized is not None:
                    child_elem = ET.Element("SW-COMPOSITION-COMPONENT-TYPE-REF")
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
    def deserialize(cls, element: ET.Element) -> "CpSoftwareCluster":
        """Deserialize XML element to CpSoftwareCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareCluster, cls).deserialize(element)

        # Parse software_cluster
        child = SerializationHelper.find_child_element(element, "SOFTWARE-CLUSTER")
        if child is not None:
            software_cluster_value = child.text
            obj.software_cluster = software_cluster_value

        # Parse sw_components (list from container "SW-COMPONENTS")
        obj.sw_components = []
        container = SerializationHelper.find_child_element(element, "SW-COMPONENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_components.append(child_value)

        # Parse sw_composition_component_type_refs (list from container "SW-COMPOSITION-COMPONENT-TYPE-REFS")
        obj.sw_composition_component_type_refs = []
        container = SerializationHelper.find_child_element(element, "SW-COMPOSITION-COMPONENT-TYPE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_composition_component_type_refs.append(child_value)

        return obj



class CpSoftwareClusterBuilder:
    """Builder for CpSoftwareCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareCluster = CpSoftwareCluster()

    def build(self) -> CpSoftwareCluster:
        """Build and return CpSoftwareCluster object.

        Returns:
            CpSoftwareCluster instance
        """
        # TODO: Add validation
        return self._obj
