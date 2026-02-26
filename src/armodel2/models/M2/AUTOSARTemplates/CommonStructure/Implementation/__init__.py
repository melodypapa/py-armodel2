"""Implementation module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
        ImplementationProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
        Implementation,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.code import (
        Code,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
        DependencyOnArtifact,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.compiler import (
        Compiler,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.linker import (
        Linker,
    )

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_usage_enum import (
    DependencyUsageEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.programminglanguage_enum import (
    ProgramminglanguageEnum,
)

__all__ = [
    "Code",
    "Compiler",
    "DependencyOnArtifact",
    "DependencyUsageEnum",
    "Implementation",
    "ImplementationProps",
    "Linker",
    "ProgramminglanguageEnum",
]
