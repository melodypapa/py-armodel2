"""SenderReceiverAnnotation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SenderReceiverAnnotation(GeneralAnnotation):
    """AUTOSAR SenderReceiverAnnotation."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "computed": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # computed
        "data_element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # dataElement
        "limit_kind": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataLimitKindEnum,
        ),  # limitKind
        "processing_kind_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ProcessingKindEnum,
        ),  # processingKindEnum
    }

    def __init__(self) -> None:
        """Initialize SenderReceiverAnnotation."""
        super().__init__()
        self.computed: Optional[Boolean] = None
        self.data_element: Optional[VariableDataPrototype] = None
        self.limit_kind: Optional[DataLimitKindEnum] = None
        self.processing_kind_enum: Optional[ProcessingKindEnum] = None


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
