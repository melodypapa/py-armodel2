"""AUTOSAR AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 301)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 298)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 287)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 59)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 968)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1993)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 203)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 30)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 42)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 71)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 421)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 29)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 56)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 157)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AutosarTopLevelStructure.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
    ARPackage,
)
from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (
    AdminData,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.file_info_comment import (
    FileInfoComment,
)


class AUTOSAR(ARObject):
    """AUTOSAR AUTOSAR."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "admin_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AdminData,
        ),  # adminData
        "ar_packages": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ARPackage,
        ),  # arPackages
        "file_info": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FileInfoComment,
        ),  # fileInfo
        "introduction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # introduction
    }

    def __init__(self) -> None:
        """Initialize AUTOSAR."""
        super().__init__()
        self.admin_data: Optional[AdminData] = None
        self.ar_packages: list[ARPackage] = []
        self.file_info: Optional[FileInfoComment] = None
        self.introduction: Optional[DocumentationBlock] = None


class AUTOSARBuilder:
    """Builder for AUTOSAR."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AUTOSAR = AUTOSAR()

    def build(self) -> AUTOSAR:
        """Build and return AUTOSAR object.

        Returns:
            AUTOSAR instance
        """
        # TODO: Add validation
        return self._obj
