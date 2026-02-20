"""DiagnosticEcuInstanceProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 207)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import (
    DiagnosticObdSupportEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class DiagnosticEcuInstanceProps(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEcuInstanceProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecu_instance_refs: list[ARRef]
    obd_support: Optional[DiagnosticObdSupportEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticEcuInstanceProps."""
        super().__init__()
        self.ecu_instance_refs: list[ARRef] = []
        self.obd_support: Optional[DiagnosticObdSupportEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEcuInstanceProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEcuInstanceProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecu_instance_refs (list to container "ECU-INSTANCE-REFS")
        if self.ecu_instance_refs:
            wrapper = ET.Element("ECU-INSTANCE-REFS")
            for item in self.ecu_instance_refs:
                serialized = ARObject._serialize_item(item, "EcuInstance")
                if serialized is not None:
                    child_elem = ET.Element("ECU-INSTANCE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize obd_support
        if self.obd_support is not None:
            serialized = ARObject._serialize_item(self.obd_support, "DiagnosticObdSupportEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OBD-SUPPORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEcuInstanceProps":
        """Deserialize XML element to DiagnosticEcuInstanceProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEcuInstanceProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEcuInstanceProps, cls).deserialize(element)

        # Parse ecu_instance_refs (list from container "ECU-INSTANCE-REFS")
        obj.ecu_instance_refs = []
        container = ARObject._find_child_element(element, "ECU-INSTANCE-REFS")
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
                    obj.ecu_instance_refs.append(child_value)

        # Parse obd_support
        child = ARObject._find_child_element(element, "OBD-SUPPORT")
        if child is not None:
            obd_support_value = DiagnosticObdSupportEnum.deserialize(child)
            obj.obd_support = obd_support_value

        return obj



class DiagnosticEcuInstancePropsBuilder:
    """Builder for DiagnosticEcuInstanceProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEcuInstanceProps = DiagnosticEcuInstanceProps()

    def build(self) -> DiagnosticEcuInstanceProps:
        """Build and return DiagnosticEcuInstanceProps object.

        Returns:
            DiagnosticEcuInstanceProps instance
        """
        # TODO: Add validation
        return self._obj
