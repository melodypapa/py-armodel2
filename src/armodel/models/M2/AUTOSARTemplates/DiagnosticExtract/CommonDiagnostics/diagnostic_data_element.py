"""DiagnosticDataElement AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class DiagnosticDataElement(Identifiable):
    """AUTOSAR DiagnosticDataElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "array_size": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ArraySizeSemanticsEnum,
        ),  # arraySize
        "max_number_of": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxNumberOf
        "scaling_info_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # scalingInfoSize
        "sw_data_def": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # swDataDef
    }

    def __init__(self) -> None:
        """Initialize DiagnosticDataElement."""
        super().__init__()
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.max_number_of: Optional[PositiveInteger] = None
        self.scaling_info_size: Optional[PositiveInteger] = None
        self.sw_data_def: Optional[SwDataDefProps] = None


class DiagnosticDataElementBuilder:
    """Builder for DiagnosticDataElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataElement = DiagnosticDataElement()

    def build(self) -> DiagnosticDataElement:
        """Build and return DiagnosticDataElement object.

        Returns:
            DiagnosticDataElement instance
        """
        # TODO: Add validation
        return self._obj
