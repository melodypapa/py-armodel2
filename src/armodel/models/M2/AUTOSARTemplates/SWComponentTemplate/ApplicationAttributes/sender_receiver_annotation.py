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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverAnnotation":
        """Deserialize XML element to SenderReceiverAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverAnnotation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse computed
        child = ARObject._find_child_element(element, "COMPUTED")
        if child is not None:
            computed_value = child.text
            obj.computed = computed_value

        # Parse data_element_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT")
        if child is not None:
            data_element_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.data_element_ref = data_element_ref_value

        # Parse limit_kind
        child = ARObject._find_child_element(element, "LIMIT-KIND")
        if child is not None:
            limit_kind_value = child.text
            obj.limit_kind = limit_kind_value

        # Parse processing_kind_enum
        child = ARObject._find_child_element(element, "PROCESSING-KIND-ENUM")
        if child is not None:
            processing_kind_enum_value = child.text
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
