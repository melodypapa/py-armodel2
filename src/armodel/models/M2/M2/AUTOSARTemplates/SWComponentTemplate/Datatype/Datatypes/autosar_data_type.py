"""AutosarDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 231)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2001)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class AutosarDataType(ARElement):
    """AUTOSAR AutosarDataType."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sw_data_def": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # swDataDef
    }

    def __init__(self) -> None:
        """Initialize AutosarDataType."""
        super().__init__()
        self.sw_data_def: Optional[SwDataDefProps] = None


class AutosarDataTypeBuilder:
    """Builder for AutosarDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarDataType = AutosarDataType()

    def build(self) -> AutosarDataType:
        """Build and return AutosarDataType object.

        Returns:
            AutosarDataType instance
        """
        # TODO: Add validation
        return self._obj
