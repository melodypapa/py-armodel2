"""SenderReceiverAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 152)

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
    DataLimitKindEnum,
    ProcessingKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from abc import ABC, abstractmethod


class SenderReceiverAnnotation(GeneralAnnotation, ABC):
    """AUTOSAR SenderReceiverAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    computed: Optional[Boolean]
    data_element_ref: Optional[ARRef]
    limit_kind: Optional[DataLimitKindEnum]
    processing_kind_enum: Optional[ProcessingKindEnum]
    def __init__(self) -> None:
        """Initialize SenderReceiverAnnotation."""
        super().__init__()
        self.computed: Optional[Boolean] = None
        self.data_element_ref: Optional[ARRef] = None
        self.limit_kind: Optional[DataLimitKindEnum] = None
        self.processing_kind_enum: Optional[ProcessingKindEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize SenderReceiverAnnotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderReceiverAnnotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize computed
        if self.computed is not None:
            serialized = ARObject._serialize_item(self.computed, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPUTED")
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

        # Serialize limit_kind
        if self.limit_kind is not None:
            serialized = ARObject._serialize_item(self.limit_kind, "DataLimitKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIMIT-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize processing_kind_enum
        if self.processing_kind_enum is not None:
            serialized = ARObject._serialize_item(self.processing_kind_enum, "ProcessingKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSING-KIND-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverAnnotation":
        """Deserialize XML element to SenderReceiverAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderReceiverAnnotation, cls).deserialize(element)

        # Parse computed
        child = ARObject._find_child_element(element, "COMPUTED")
        if child is not None:
            computed_value = child.text
            obj.computed = computed_value

        # Parse data_element_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT-REF")
        if child is not None:
            data_element_ref_value = ARRef.deserialize(child)
            obj.data_element_ref = data_element_ref_value

        # Parse limit_kind
        child = ARObject._find_child_element(element, "LIMIT-KIND")
        if child is not None:
            limit_kind_value = DataLimitKindEnum.deserialize(child)
            obj.limit_kind = limit_kind_value

        # Parse processing_kind_enum
        child = ARObject._find_child_element(element, "PROCESSING-KIND-ENUM")
        if child is not None:
            processing_kind_enum_value = ProcessingKindEnum.deserialize(child)
            obj.processing_kind_enum = processing_kind_enum_value

        return obj



class SenderReceiverAnnotationBuilder:
    """Builder for SenderReceiverAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderReceiverAnnotation = SenderReceiverAnnotation()

    def build(self) -> SenderReceiverAnnotation:
        """Build and return SenderReceiverAnnotation object.

        Returns:
            SenderReceiverAnnotation instance
        """
        # TODO: Add validation
        return self._obj
