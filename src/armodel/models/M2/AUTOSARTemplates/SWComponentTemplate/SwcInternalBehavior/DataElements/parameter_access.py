"""ParameterAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 586)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
        AutosarParameterRef,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class ParameterAccess(AbstractAccessPoint):
    """AUTOSAR ParameterAccess."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "accessed_parameter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class="AutosarParameterRef",
        ),  # accessedParameter
        "sw_data_def": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class="SwDataDefProps",
        ),  # swDataDef
    }

    def __init__(self) -> None:
        """Initialize ParameterAccess."""
        super().__init__()
        self.accessed_parameter: Optional[AutosarParameterRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None


class ParameterAccessBuilder:
    """Builder for ParameterAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterAccess = ParameterAccess()

    def build(self) -> ParameterAccess:
        """Build and return ParameterAccess object.

        Returns:
            ParameterAccess instance
        """
        # TODO: Add validation
        return self._obj
