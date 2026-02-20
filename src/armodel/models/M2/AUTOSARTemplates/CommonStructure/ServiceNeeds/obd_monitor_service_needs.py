"""ObdMonitorServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 797)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticMonitorUpdateKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)


class ObdMonitorServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdMonitorServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_data_ref: Optional[ARRef]
    event_needs_ref: Optional[ARRef]
    unit_and_scaling_id: Optional[PositiveInteger]
    update_kind: Optional[DiagnosticMonitorUpdateKindEnum]
    def __init__(self) -> None:
        """Initialize ObdMonitorServiceNeeds."""
        super().__init__()
        self.application_data_ref: Optional[ARRef] = None
        self.event_needs_ref: Optional[ARRef] = None
        self.unit_and_scaling_id: Optional[PositiveInteger] = None
        self.update_kind: Optional[DiagnosticMonitorUpdateKindEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize ObdMonitorServiceNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ObdMonitorServiceNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application_data_ref
        if self.application_data_ref is not None:
            serialized = ARObject._serialize_item(self.application_data_ref, "ApplicationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_needs_ref
        if self.event_needs_ref is not None:
            serialized = ARObject._serialize_item(self.event_needs_ref, "DiagnosticEventNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-NEEDS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unit_and_scaling_id
        if self.unit_and_scaling_id is not None:
            serialized = ARObject._serialize_item(self.unit_and_scaling_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT-AND-SCALING-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize update_kind
        if self.update_kind is not None:
            serialized = ARObject._serialize_item(self.update_kind, "DiagnosticMonitorUpdateKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPDATE-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdMonitorServiceNeeds":
        """Deserialize XML element to ObdMonitorServiceNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ObdMonitorServiceNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ObdMonitorServiceNeeds, cls).deserialize(element)

        # Parse application_data_ref
        child = ARObject._find_child_element(element, "APPLICATION-DATA-REF")
        if child is not None:
            application_data_ref_value = ARRef.deserialize(child)
            obj.application_data_ref = application_data_ref_value

        # Parse event_needs_ref
        child = ARObject._find_child_element(element, "EVENT-NEEDS-REF")
        if child is not None:
            event_needs_ref_value = ARRef.deserialize(child)
            obj.event_needs_ref = event_needs_ref_value

        # Parse unit_and_scaling_id
        child = ARObject._find_child_element(element, "UNIT-AND-SCALING-ID")
        if child is not None:
            unit_and_scaling_id_value = child.text
            obj.unit_and_scaling_id = unit_and_scaling_id_value

        # Parse update_kind
        child = ARObject._find_child_element(element, "UPDATE-KIND")
        if child is not None:
            update_kind_value = DiagnosticMonitorUpdateKindEnum.deserialize(child)
            obj.update_kind = update_kind_value

        return obj



class ObdMonitorServiceNeedsBuilder:
    """Builder for ObdMonitorServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ObdMonitorServiceNeeds = ObdMonitorServiceNeeds()

    def build(self) -> ObdMonitorServiceNeeds:
        """Build and return ObdMonitorServiceNeeds object.

        Returns:
            ObdMonitorServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
