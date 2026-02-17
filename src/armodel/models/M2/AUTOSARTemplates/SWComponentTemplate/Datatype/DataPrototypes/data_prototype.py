"""DataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 305)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2013)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class DataPrototype(Identifiable):
    """AUTOSAR DataPrototype."""
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
        """Initialize DataPrototype."""
        super().__init__()
        self.sw_data_def: Optional[SwDataDefProps] = None


class DataPrototypeBuilder:
    """Builder for DataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototype = DataPrototype()

    def build(self) -> DataPrototype:
        """Build and return DataPrototype object.

        Returns:
            DataPrototype instance
        """
        # TODO: Add validation
        return self._obj
