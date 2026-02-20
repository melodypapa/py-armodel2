"""IoHwAbstractionServerAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    FilterDebouncingEnum,
    PulseTestEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
        PortPrototype,
    )



class IoHwAbstractionServerAnnotation(GeneralAnnotation):
    """AUTOSAR IoHwAbstractionServerAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    age: Optional[MultidimensionalTime]
    argument_ref: Optional[ARRef]
    bsw_resolution: Optional[Float]
    data_element_ref: Optional[ARRef]
    failure_ref: Optional[ARRef]
    filtering: Optional[FilterDebouncingEnum]
    pulse_test: Optional[PulseTestEnum]
    trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize IoHwAbstractionServerAnnotation."""
        super().__init__()
        self.age: Optional[MultidimensionalTime] = None
        self.argument_ref: Optional[ARRef] = None
        self.bsw_resolution: Optional[Float] = None
        self.data_element_ref: Optional[ARRef] = None
        self.failure_ref: Optional[ARRef] = None
        self.filtering: Optional[FilterDebouncingEnum] = None
        self.pulse_test: Optional[PulseTestEnum] = None
        self.trigger_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize IoHwAbstractionServerAnnotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IoHwAbstractionServerAnnotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize age
        if self.age is not None:
            serialized = ARObject._serialize_item(self.age, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize argument_ref
        if self.argument_ref is not None:
            serialized = ARObject._serialize_item(self.argument_ref, "ArgumentDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARGUMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bsw_resolution
        if self.bsw_resolution is not None:
            serialized = ARObject._serialize_item(self.bsw_resolution, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-RESOLUTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = ARObject._serialize_item(self.data_element_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize failure_ref
        if self.failure_ref is not None:
            serialized = ARObject._serialize_item(self.failure_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FAILURE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filtering
        if self.filtering is not None:
            serialized = ARObject._serialize_item(self.filtering, "FilterDebouncingEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTERING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pulse_test
        if self.pulse_test is not None:
            serialized = ARObject._serialize_item(self.pulse_test, "PulseTestEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PULSE-TEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_ref
        if self.trigger_ref is not None:
            serialized = ARObject._serialize_item(self.trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IoHwAbstractionServerAnnotation":
        """Deserialize XML element to IoHwAbstractionServerAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IoHwAbstractionServerAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IoHwAbstractionServerAnnotation, cls).deserialize(element)

        # Parse age
        child = ARObject._find_child_element(element, "AGE")
        if child is not None:
            age_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.age = age_value

        # Parse argument_ref
        child = ARObject._find_child_element(element, "ARGUMENT-REF")
        if child is not None:
            argument_ref_value = ARRef.deserialize(child)
            obj.argument_ref = argument_ref_value

        # Parse bsw_resolution
        child = ARObject._find_child_element(element, "BSW-RESOLUTION")
        if child is not None:
            bsw_resolution_value = child.text
            obj.bsw_resolution = bsw_resolution_value

        # Parse data_element_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT-REF")
        if child is not None:
            data_element_ref_value = ARRef.deserialize(child)
            obj.data_element_ref = data_element_ref_value

        # Parse failure_ref
        child = ARObject._find_child_element(element, "FAILURE-REF")
        if child is not None:
            failure_ref_value = ARRef.deserialize(child)
            obj.failure_ref = failure_ref_value

        # Parse filtering
        child = ARObject._find_child_element(element, "FILTERING")
        if child is not None:
            filtering_value = FilterDebouncingEnum.deserialize(child)
            obj.filtering = filtering_value

        # Parse pulse_test
        child = ARObject._find_child_element(element, "PULSE-TEST")
        if child is not None:
            pulse_test_value = PulseTestEnum.deserialize(child)
            obj.pulse_test = pulse_test_value

        # Parse trigger_ref
        child = ARObject._find_child_element(element, "TRIGGER-REF")
        if child is not None:
            trigger_ref_value = ARRef.deserialize(child)
            obj.trigger_ref = trigger_ref_value

        return obj



class IoHwAbstractionServerAnnotationBuilder:
    """Builder for IoHwAbstractionServerAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IoHwAbstractionServerAnnotation = IoHwAbstractionServerAnnotation()

    def build(self) -> IoHwAbstractionServerAnnotation:
        """Build and return IoHwAbstractionServerAnnotation object.

        Returns:
            IoHwAbstractionServerAnnotation instance
        """
        # TODO: Add validation
        return self._obj
