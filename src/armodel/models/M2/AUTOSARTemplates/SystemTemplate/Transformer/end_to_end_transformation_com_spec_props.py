"""EndToEndTransformationComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 200)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2023)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
    TransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.e2_e_profile_compatibility_props import (
    E2EProfileCompatibilityProps,
)


class EndToEndTransformationComSpecProps(TransformationComSpecProps):
    """AUTOSAR EndToEndTransformationComSpecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    clear_from_valid: Optional[Boolean]
    disable_end_to: Optional[Boolean]
    e2e_profile_ref: Optional[ARRef]
    max_delta: Optional[PositiveInteger]
    max_error_state: Optional[PositiveInteger]
    max_no_new_or: Optional[PositiveInteger]
    min_ok_state_init: Optional[PositiveInteger]
    min_ok_state: Optional[PositiveInteger]
    sync_counter_init: Optional[PositiveInteger]
    window_size_init: Optional[PositiveInteger]
    window_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EndToEndTransformationComSpecProps."""
        super().__init__()
        self.clear_from_valid: Optional[Boolean] = None
        self.disable_end_to: Optional[Boolean] = None
        self.e2e_profile_ref: Optional[ARRef] = None
        self.max_delta: Optional[PositiveInteger] = None
        self.max_error_state: Optional[PositiveInteger] = None
        self.max_no_new_or: Optional[PositiveInteger] = None
        self.min_ok_state_init: Optional[PositiveInteger] = None
        self.min_ok_state: Optional[PositiveInteger] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.window_size_init: Optional[PositiveInteger] = None
        self.window_size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EndToEndTransformationComSpecProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EndToEndTransformationComSpecProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize clear_from_valid
        if self.clear_from_valid is not None:
            serialized = SerializationHelper.serialize_item(self.clear_from_valid, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLEAR-FROM-VALID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize disable_end_to
        if self.disable_end_to is not None:
            serialized = SerializationHelper.serialize_item(self.disable_end_to, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DISABLE-END-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize e2e_profile_ref
        if self.e2e_profile_ref is not None:
            serialized = SerializationHelper.serialize_item(self.e2e_profile_ref, "E2EProfileCompatibilityProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("E2E-PROFILE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_delta
        if self.max_delta is not None:
            serialized = SerializationHelper.serialize_item(self.max_delta, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-DELTA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_error_state
        if self.max_error_state is not None:
            serialized = SerializationHelper.serialize_item(self.max_error_state, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-ERROR-STATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_no_new_or
        if self.max_no_new_or is not None:
            serialized = SerializationHelper.serialize_item(self.max_no_new_or, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NO-NEW-OR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_ok_state_init
        if self.min_ok_state_init is not None:
            serialized = SerializationHelper.serialize_item(self.min_ok_state_init, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-OK-STATE-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_ok_state
        if self.min_ok_state is not None:
            serialized = SerializationHelper.serialize_item(self.min_ok_state, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-OK-STATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_counter_init
        if self.sync_counter_init is not None:
            serialized = SerializationHelper.serialize_item(self.sync_counter_init, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-COUNTER-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize window_size_init
        if self.window_size_init is not None:
            serialized = SerializationHelper.serialize_item(self.window_size_init, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WINDOW-SIZE-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize window_size
        if self.window_size is not None:
            serialized = SerializationHelper.serialize_item(self.window_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WINDOW-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndTransformationComSpecProps":
        """Deserialize XML element to EndToEndTransformationComSpecProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndTransformationComSpecProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndTransformationComSpecProps, cls).deserialize(element)

        # Parse clear_from_valid
        child = SerializationHelper.find_child_element(element, "CLEAR-FROM-VALID")
        if child is not None:
            clear_from_valid_value = child.text
            obj.clear_from_valid = clear_from_valid_value

        # Parse disable_end_to
        child = SerializationHelper.find_child_element(element, "DISABLE-END-TO")
        if child is not None:
            disable_end_to_value = child.text
            obj.disable_end_to = disable_end_to_value

        # Parse e2e_profile_ref
        child = SerializationHelper.find_child_element(element, "E2E-PROFILE-REF")
        if child is not None:
            e2e_profile_ref_value = ARRef.deserialize(child)
            obj.e2e_profile_ref = e2e_profile_ref_value

        # Parse max_delta
        child = SerializationHelper.find_child_element(element, "MAX-DELTA")
        if child is not None:
            max_delta_value = child.text
            obj.max_delta = max_delta_value

        # Parse max_error_state
        child = SerializationHelper.find_child_element(element, "MAX-ERROR-STATE")
        if child is not None:
            max_error_state_value = child.text
            obj.max_error_state = max_error_state_value

        # Parse max_no_new_or
        child = SerializationHelper.find_child_element(element, "MAX-NO-NEW-OR")
        if child is not None:
            max_no_new_or_value = child.text
            obj.max_no_new_or = max_no_new_or_value

        # Parse min_ok_state_init
        child = SerializationHelper.find_child_element(element, "MIN-OK-STATE-INIT")
        if child is not None:
            min_ok_state_init_value = child.text
            obj.min_ok_state_init = min_ok_state_init_value

        # Parse min_ok_state
        child = SerializationHelper.find_child_element(element, "MIN-OK-STATE")
        if child is not None:
            min_ok_state_value = child.text
            obj.min_ok_state = min_ok_state_value

        # Parse sync_counter_init
        child = SerializationHelper.find_child_element(element, "SYNC-COUNTER-INIT")
        if child is not None:
            sync_counter_init_value = child.text
            obj.sync_counter_init = sync_counter_init_value

        # Parse window_size_init
        child = SerializationHelper.find_child_element(element, "WINDOW-SIZE-INIT")
        if child is not None:
            window_size_init_value = child.text
            obj.window_size_init = window_size_init_value

        # Parse window_size
        child = SerializationHelper.find_child_element(element, "WINDOW-SIZE")
        if child is not None:
            window_size_value = child.text
            obj.window_size = window_size_value

        return obj



class EndToEndTransformationComSpecPropsBuilder:
    """Builder for EndToEndTransformationComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndTransformationComSpecProps = EndToEndTransformationComSpecProps()

    def build(self) -> EndToEndTransformationComSpecProps:
        """Build and return EndToEndTransformationComSpecProps object.

        Returns:
            EndToEndTransformationComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
