"""SystemSignal AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 332)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1009)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 218)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class SystemSignal(ARElement):
    """AUTOSAR SystemSignal."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dynamic_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dynamicLength
        "physical_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # physicalProps
    }

    def __init__(self) -> None:
        """Initialize SystemSignal."""
        super().__init__()
        self.dynamic_length: Optional[Boolean] = None
        self.physical_props: Optional[SwDataDefProps] = None


class SystemSignalBuilder:
    """Builder for SystemSignal."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemSignal = SystemSignal()

    def build(self) -> SystemSignal:
        """Build and return SystemSignal object.

        Returns:
            SystemSignal instance
        """
        # TODO: Add validation
        return self._obj
